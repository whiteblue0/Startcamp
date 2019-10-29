// 변수와 식별자
/*
var x = 1

if (x === 1){
  var x = 2
  console.log(x)
}
console.log(x)


// let -> 값을 재할당 할 수 있는 변수 선언 키워드(선언ㄴ은 한번만, 할당은 여러번 가능)
let x = 1
console.log(x)
x = 2
console.log(x)

let x = 1
if (x ===1 ){
  let x = 2
  console.log(x)
}
console.log(x)

// const = 상수 : 값이 변하지 않는 상수를 선언하는 키워드
// 담긴 값이 변하지 않는 것이 아니라 상수의 값은 재할당을 통해 바뀔 수 없고 재선언 될 수 없다.

const MY_FAV = 7
console.log(MY_FAV)
console.log("my favorite number is "+ MY_FAV)
// MY_FAV = 20


const MY_FAV = 7
if (MY_FAV === 7){
  const MY_FAV = 20
  console.log("my favorite number is "+ MY_FAV)
}
console.log(MY_FAV)


// let 과 var 의 scope 비교

// var
function varTest(){
  var x = 1
  if (true){
    var x = 2
    console.log(x)
  }
  console.log(x)
}
varTest()


// let
function letTest(){
  let x = 1
  if (true){
    let x = 2
    console.log(x)
  }
  console.log(x)
}

letTest()


var a = 1
var b = 2

if (a ===1 ){
  var a = 11
  let b = 22
  console.log(a)
  console.log(b)
}
console.log(a)
console.log(b)

// var: 할당 및 선언 자유, 함수 스코프
// let: 할당 자유, 선언은 한번만, 블록 스코프
// const: 할당 및 선언 한번만, 블록 스코프


// 변수와 식별자
// 객체, 변수, 함수 -> lower-camel-case 사용

// 숫자,문자,boolen
let dog
let variableName

// 객체
const memeberInfo = {
  id:1,
  password:12345,
  gender:'male',
}
// 배열 - 복수형을 사용

const dogs = []

// 정규 표현식 - 'r'로 시작

const rDesc = /ab+c/

// 함수
funcion getPropertyName() {
  
}

// 이벤트 핸들러 - 이벤트 핸들러는 'on'으로 시작

const onClick = () => {}
const onKeyDown = () => {}

//  boolen 반환하는 함수-> return값이 boolen인 함수는 'is'로 시작
let isAvailable = false

// 파스칼 케이스(upper-camel-case)

class User {
  constructor(optoins){
    this.name = optoins.name
  }
}

const good = new User({
  name: 'yup',
})

console.log(good)
console.log(typeof good)
*/
// 대문자 스네이크 케이스 - 상수
export const API_KEY = 'SOMEKEY'

export const MAPPING =  {
  key: 'value'
}