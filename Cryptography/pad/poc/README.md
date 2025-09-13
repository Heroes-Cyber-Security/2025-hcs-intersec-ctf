# Proof of Concept

https://medium.com/@olyhossen10/breaking-aes-cbc-with-a-noisy-padding-oracle-48a82f570e98

1. Each "Unpad" query returns `pad = 0` or `1`, but with noise—e.g., valid padding yields `pad = 0` about 80% of the time. We treat `pad = 0` as an indication of "valid padding".

2. For each candidate ciphertext:
   - Query “Unpad” multiple times (e.g., 21).
   - Stop early when a majority decision is clear (after at least 7 samples).
   - This majority mechanism effectively filters out noise.

3. For each block (e.g., decrypting C₂ using C₁):
   - Work from the last byte (pad = 1) back to the first:
     - For each candidate guess `g` (0–255, prioritized over ASCII-hex values):
       - Compute a modified previous block so that decryption of C₂ ends in padding byte equal to current pad value.
       - Query the noisy oracle via the majority vote.
       - When oracle indicates valid padding, derive the intermediate byte and hence the plaintext byte.
   - Repeat for all bytes and both blocks (`C₂` using `C₁`, then `C₁` using `IV`), yielding the full plaintext.