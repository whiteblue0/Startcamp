// function

/*
// 선언식
function add(num1, num2){
  return num1 + num2
}

console.log(add(2,7))

const sub = function(num1,num2){
  return num1 - num2
}

console.log(sub(7,2))

// JS에서 함수도 하나의 값(객체)
console.log(typeof add)
console.log(typeof sub)


// Arrow function
// 쓰는 이유
// Arrow function은 항상 익명 함수이다.
// 1. function keword 생략가능
// 2. 함수의 매개변수가 1개일때는 괄호 생략가능
// 3. 함수 바디의 표현식이 하나라면 {}와 return 생략 가능

// 함수 표현식
// const ssafy1 = function(){
//   return 'hello'
// }
// console.log(ssafy1())
// Arrow function으로 변환
// 1. function 키워드 삭제가능
const ssafy1 = (name) => {return `Hello! ${name}`}
console.log(ssafy1('justin'))

// 2. 인자가 1개 있을 때 ()를 생략 가능
const ssafy1 = name => {return `Hello! ${name}`}

console.log(ssafy1('justin'))


// 3. {}와 return 생략
const ssafy1 = name => {return `Hello! ${name}`}



// let square = function(num){
//   return num ** 2
// }

let square  = num =>  num**2
console.log(square)

// 4. 인자가 없을 때 -> (), _표현 가능
let noArgs = () => 'noArges'
console.log(noArgs())
noArgs = _ => 'noArges'
console.log(noArgs())



// 5-1. object 리턴하려면?
let returnObject = () => {return {key:'value'}}
console.log(returnObject())
console.log(typeof returnObject())

5-2. return 을 적지 않으면?
returnObject = () => {key:'value'}
console.log(returnObject())
console.log(typeof returnObject())

5-3. return문을 적지 않았을 때
returnObject = () => {key:'value'}
console.log(returnObject())
console.log(typeof returnObject())


// 기본 인자(default args)
// 기본 인자를 줄 때는 인자 개수와 상관없이 괄호를 꼭 해야 한다.
// 괄호가 없으면 syntax error 발생

const sayhello = (name='noName') => `Hi ${name}`

console.log(sayhello('justin'))
console.log(sayhello())


// 익명 함수/ 1회용 함수
// 즉시 실행 함수는 초기화에 많이 사용한다.

// function (num) { return num ** 3 }

// 1. 익명함수 -> 변수에 담아 사용(표현식)
const cube = function (num) { return num ** 3}
const squareRoot = num => num ** 0.5

console.log(cube(2))
console.log(squareRoot(4))

// 2. 즉시 실행 함수 -> 주로 초기화에 사용

console.log((function (num) { return num ** 3})(2))
console.log((num => num ** 0.5)(4))


// 함수 호이스팅

ssafy()

function ssafy(){
  console.log('hoisting!')
}

ssafy2()

let ssafy2 = function(){
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정
let ssafy2 // 1. 변수 선언 -> let은 초기화가 동시에 진행되지 않음

ssafy2() // 2. 함수 호출 -> ssafy2가 초기화가 안됨

ssafy2 = function(){
  console.log('hoisting!')
} // 3. 변수에 할당


ssafy3()

var ssafy3 = function(){
  console.log('hoisting!')
}

// JS 엔진이 코드를 해석하는 과정
var ssafy3 // 1. 변수 호이스팅(선언 + 초기화)

ssafy3() // 2. 함수 호출 -> let 과 다르게 초기값 undefined가 들어감.
// 함수를 호출하는 시점에서 ssafy3라는 변수에는 함수가 아닌 undefined가 들어있기 때문에
// TypeError: ssafy3 is not a function 라는 에러 메세지를 보냄!

ssafy3 = function(){
  console.log('hoisting!')
}

*/

