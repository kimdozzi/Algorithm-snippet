# Javascript_Syntax(업데이트 중..)

## Variable
    var i;
    var x = 123;
    var y = "123";
    var z = false;
    var w = null;

    let myname = "max"; // variable
    const name = "manu"; // unvariable

## Function
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
    
## Class
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
