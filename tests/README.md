# Test Suite Guide

The suite is meant to behave like nand2tetris:

- read a project brief,
- write the code yourself,
- run the smallest matching checkpoint until it passes,
- then run the matching visual checkpoint.

## Recommended Order

```powershell
python project_00.py avg-test
python project_00.py argmax-test
python project_00.py epsilon-test
python project_00.py bandit-test
python project_01.py return-test
python project_01.py backups-test
python project_01.py policy-test
python project_01.py value-test
```

## Notes

- Some later tests skip automatically until you install `gymnasium` or `pufferlib`.
- The early projects now include trace contracts that feed the shared raylib viewers.
- The full suite is expected to fail until you have implemented the corresponding project.
