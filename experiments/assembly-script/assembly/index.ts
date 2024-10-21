// The entry file of your WebAssembly module.

@external("", "test_callback")
declare function test_callback(n: i32): void;

export function add(a: i32, b: i32): i32 {
  return a + b;
}

export function addmul(a: i32, b: i32, c: i32): i32 {
  const result = (a + b) * c;
  test_callback(result);
  return result;
}