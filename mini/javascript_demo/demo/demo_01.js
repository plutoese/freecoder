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

for(let count = 0; count < 5; count++){
    console.log(count)
}

let data = [1, 2, 3, 4, 5, 6]; sum = 0;
for(let element of data){
    sum += element
}
console.log(sum)

let obj1 = {x: 1, y: 2, z: 3};
let keys = "";
for(let k of Object.keys(obj1)){
    keys += k
}
console.log(keys)

let o1 = Object.create({x: 1, y: 2})
console.log(o1.x + o1.y)

let o2 = Object.create(Object.prototype)
console.log(o2)

let s = {x: 1, y: 2};
console.log(s.toString())

let point = {
    x: 1,
    y: 2,
    toString: function() {return `(${this.x}, ${this.y})`}
}
console.log(point.toString())

let new_data = [1, 2, 3, 4, 5];
let new_sum = 0;
new_data.forEach(value => {new_sum += value;});
console.log(new_sum)

console.log(new_data.map(x => x * x))
