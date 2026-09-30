# Does Password Complexity Predict Security?

A safe, synthetic experiment comparing password patterns and guessing strategies. It never targets a real account and does not store real credentials.

## Research question

> Is length, character variety, or unpredictability the most useful signal against simple guessing strategies?

## Experiment design

The program generates labeled synthetic passwords, hashes them with SHA-256 only to model a lookup target, and tests three toy strategies:

- dictionary guesses
- common-pattern guesses
- bounded brute force over lowercase strings

This is **not** a password cracker and SHA-256 is **not** recommended for password storage. Production systems should use a slow password-hashing function such as Argon2id, scrypt, or bcrypt.

## Run it

```bash
python3 -m src.experiment
python3 -m unittest discover -s tests -v
```

## Curiosity prompts

- Is `Password123!` stronger than a long but predictable phrase?
- How much does adding a symbol change the experiment?
- Which strategy wins against human-style patterns?
- How would slow password hashing change attacker cost?

All passwords are generated or clearly synthetic. No plaintext credential file is committed.
## Project reflection

- **What I personally implemented:** I wrote the synthetic target categories, SHA-256 modeling helper, dictionary strategy, pattern strategy, bounded brute-force strategy, experiment runner, and unit tests.
- **One actual result:** All **4 tests passed**; the pattern strategy found the synthetic `Password123!` target in **2 guesses**, while the bounded brute-force strategy reached **205,426 attempts** for the short random target.
- **One unexpected result:** The long synthetic passphrase was found immediately by the dictionary strategy because it had accidentally been included in the dictionary, revealing target leakage in the experiment design.
- **One limitation:** The toy SHA-256 and bounded lowercase brute-force model cannot establish real-world password-cracking time or recommend a production password-storage design.
- **Next iteration:** I intend to remove dictionary target leakage, repeat the experiment across generated password categories, and compare the cost model with Argon2id or bcrypt.
