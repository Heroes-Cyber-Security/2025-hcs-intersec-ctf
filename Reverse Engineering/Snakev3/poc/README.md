# Proof of Concept

## TL;DR

Di wasm ada validator, tldr validatornya harus jalan 111,111 kali supaya flagnya mau keluar. Beberapa cara solp:
- Loop seperti di [line 106 solve.js](solve.js)
```js
    for (let i = 0; i < 111111; i++) {
      playerScore += speedSize;
      wasm.update_on_eat();
    }
```

- Gunakan solver ini (dari AI)
```js
// The wasm object is exposed by the app.js script.

// Step 1: Calculate the required number of "eats".
const targetScore = 999999;
const scorePerEat = 9;
const eatsNeeded = targetScore / scorePerEat;
console.log(`Need to eat ${eatsNeeded} times.`);

// Step 2: Initialize the wasm module with the correct seed, just like the game does.
const seed = 4000600;
wasm.init(seed);
console.log("WASM state initialized.");

// Step 3: Call update_on_eat() the required number of times.
console.log("Simulating game play...");
for (let i = 0; i < eatsNeeded; i++) {
  wasm.update_on_eat();
}
console.log("Simulation complete. The internal state should now be correct.");

// Step 4: Replicate the memory allocation and flag retrieval from app.js.
const bufferPtr = wasm.memory.buffer.byteLength;
const bufferSize = 50; // A safe size for the flag buffer
wasm.memory.grow(1); // Ensure there's enough memory
wasm.get_flag(bufferPtr);

// Step 5: Read the result from WASM memory and print it.
const flagBytes = new Uint8Array(wasm.memory.buffer, bufferPtr, bufferSize);
// Find the null terminator to get the exact string length
const nullTerminatorIndex = flagBytes.indexOf(0); 
const flag = new TextDecoder().decode(flagBytes.slice(0, nullTerminatorIndex));

console.log("Result from get_flag:", flag);
```

- Reverse engineer wasmnya, simple xor

### Flag: 
> HCS{baby_s_first_wasm}