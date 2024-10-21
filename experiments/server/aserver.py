from wasm import WasmRuntime, WasmerRuntime

class WorldServer:
    def __init__(self, wasm_runtime: WasmRuntime):
        self.wasm = wasm_runtime
        self.wasm.export_function('test_callback', self.test_callback)

    def run(self):
        print('Wasm Lab Server Started')

        self.instance = self.wasm.make_instance('../assembly-script/build/release.wasm')
        result = self.instance.exports.addmul(1, 2, 3)
        print(result)

    def test_callback(self, n: int):
        print(f"test_callback: {n}")

def main():
    wasm = WasmerRuntime()
    server = WorldServer(wasm)
    server.run()


if __name__ == '__main__':
    main()