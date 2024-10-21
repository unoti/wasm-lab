from abc import ABC, abstractmethod
from wasmer import engine, Store, Module, Instance, ImportObject, Function
#from wasmer_compiler_llvm import Compiler
from wasmer_compiler_cranelift import Compiler

class WasmRuntime(ABC):
    @abstractmethod
    def make_instance(self, name: str):
        """Create an instance of the given module name."""

    @abstractmethod
    def export_function(self, func_name: str, implementation: any):
        """Export a locally hosted function into webassembly modules."""

class WasmerRuntime(WasmRuntime):
    def __init__(self):
        self._modules = {} # Module objects keyed by module filename.
        self._store = Store(engine.JIT(Compiler))
        self._import_object = ImportObject() # Holds info about imported functions.

    def export_function(self, func_name: str, implementation: any):
        host_function = Function(self._store, implementation)
        self._import_object.register("", {func_name: host_function})

    def make_instance(self, name: str):
        module = self._modules.get(name)
        if not module:
            content = open(name, 'rb').read()
            module = Module(self._store, content)
            self._modules[name] = module
        instance = Instance(module, self._import_object)
        return instance