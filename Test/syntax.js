var i;
var x = 123;
var y = "123";
var z = false;
var w = null;

let myname = "max"; // variable
const name = "manu"; // unvariable

const printmyname = (name, age) => {
  //인수가 없다면 () , 인수가 하나라면 name or (name)
  console.log(name, age);
};
/*
const multiply = (number) => { 
return number * 2;
}
*/

const multiply = (number) => number * 2;
console.log(multiply(2));

let add = (value1, value2) => value1 + value2;
console.log(add(10, 20));

class Human {
  constructor() {
    this.gender = "male";
  }

  printGender() {
    console.log(this.gender);
  }
}

class Person extends Human {
  constructor() {
    super();
    this.name = "max";
    this.gender = "female";
  }

  printMyname() {
    console.log(this.name);
  }
}

const person = new Person();
person.printMyname();
person.printGender();



const numbers =[1,2,3];
const newNumbers = [...numbers, 4];
console.log(newNumbers);
const xNumbers = [numbers, 4];
console.log(xNumbers);

const person1 = {
  name : 'max',
  grade : 'A'
  
};

const newPerson = {
  ...person1,
  age : 28
};

console.log(newPerson)

const numbers1 = [1,2,3];
[num1, ,num3] =numbers1;
console.log(num1,num2);








const person2 = {
  name : 'max' 
};

// secondPerson = person; 포인터 참조, 가짜 복사 
const secondPerson = { //진짜 복사
    ...person2
};

person2.name = 'Menu';

console.log(secondPerson);

// 객체와 배열은 참조 타입, 값이 아니라 포인터를 복사하는 것 ! 
// 실제로 복사하고 싶으면 새 객체를 만들고 속성만 복사해야 한다. 


/* const numbers = [1,2,3];

const doubleArr = numbers.map((num) => {
  return num * 2;
});

console.log(doubleArr);

                       */