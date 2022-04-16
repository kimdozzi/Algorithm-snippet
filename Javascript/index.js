// 백틱(`)을 사용 - 템플릿 리터럴 
var template = `hello
world.`;
console.log(template);

// before ES6
var first = 'dohyung';
var last = 'kim';

console.log('my name is ' + last + first + '.');

// After ES6 -> 표현식 삽입
var f = 'dohyung';
var l = 'kim';

console.log(`my name is ${f} ${l} .`);

// Symbol Type
var key = Symbol('key');
console.log(typeof key);

var obj = {};
obj[key] = 'value';
console.log(key);

console.log(`${obj} ${obj[key]}`);



console.log(-0 === +0);
console.log(Object.is(-0,+0));

var x = 2;
var result = (x%2==0) ? '짝수' : '홀수';
console.log(result);
