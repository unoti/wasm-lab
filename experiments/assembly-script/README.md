# Assemblyscript getting started

* [Getting started at AssemblyScript.org](https://www.assemblyscript.org/getting-started.html#setting-up-a-new-project)


I installed it using `npm init` and `npm install --save-dev assemblyscript`.

Then npx asinit .

## Directories
* `./assembly` - AssemblyScript sources to be compiled to WebAssembly
    * `tsconfig.json` - Typescript config inferiting recommended AssemblyScript settings
    * `index.ts` - Example entry file compiled to WebAssembly to get started
* `./build` - compiled webassembly files
* `./asconfig.json` Config file defining both 'debug' and 'release' targets.
* `./package.json` Package info and commands to compile to WebAssembly
* `./tests/index.js` - Test for checking that the module is functioning
* `./index.html` - Starter file loading the module in a browser

Try it
* `npm run asbuild`
* `npm test`