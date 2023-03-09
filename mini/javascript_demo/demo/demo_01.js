const a = 3
console.log(a)

const b = Math.pow(2, 4)
console.log(b)

console.log(Number.POSITIVE_INFINITY)
console.log(isNaN(NaN))

console.log(Date.now().toLocaleString())

let msg = "Hello World"
console.log(msg.concat("!"))

let name = "Bill"
console.log(`Hello ${name}!`)

let text = "testing: 1, 2, 3"
let pattern = /\d+/g
console.log(pattern.test(text))
console.log(text.match(pattern))

console.log(a === 3)

let obj = {x: 1}
obj.x = 2
console.log(obj)

console.log(parseInt("3Hello"))

let [x, ...y] = [1, 2];
[x, y] = [y, x]
console.log([x, y])

let square = function(x) {return x * x;};
console.log(square(3))

let x1 = {b: null}
console.log(x1.a)