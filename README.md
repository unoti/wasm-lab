# wasm-lab
Playground for exploring distributed processing ideas using webassembly.

## Goal
Our goal is to explore ideas of creating virtual worlds and games, where components are programmed in any programming language that can compile to webassembly.

We will explore these concepts:
* Running the core world server loop decoupled from the instantiated modules, and communicating with message queues
* Develop needed infrastructure code to make creating these modules easy
* Running modules at scale. Can we run enough concurrent instances of webassembly modules to make the idea work?
