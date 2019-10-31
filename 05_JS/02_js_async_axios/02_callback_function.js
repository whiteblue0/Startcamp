/*
// 배열로 이루어진 숫자들을 다 더하는 함수
const numbersAddEach = numbers =>{
  let sum = 0
  for (const number of numbers){
    sum += number
  }
  return sum
}

console.log(numbersAddEach([1,2,3,4,5]))


// 배열로 이루어진 숫자들을 다 빼는 함수
const numbersSubEach = numbers => {
  let sub = 0
  for (const number of numbers) {
    sub -= number
  }
  return sub
}

console.log(numbersSubEach([1,2,3,4,5]))



// 배열로 이루어진 숫자들을 다 곱하는 함수
const numbersMultipleEach = numbers => {
  let multiple = 1
  for (const number of numbers) {
    multiple *= number
  }
  return multiple
}

console.log(numbersMultipleEach([1,2,3,4,5]))



// 숫자로 이루어진 배열의 요소를 [???]한다

const NUMBERS = [1,2,3,4,5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number,acc)
  }
  return acc
}

// 더하기
const addEach = (number,acc = 0) => {
  return acc + number
}

console.log(numbersEach(NUMBERS,addEach))

// 빼기
const subEach = (number,acc = 0) => {
  return acc - number
}
console.log(numbersEach(NUMBERS,subEach))

// 곱하기
const mulEach = (number,acc = 1) => {
  return acc * number
}

console.log(numbersEach(NUMBERS,mulEach))

*/

const NUMBERS = [1,2,3,4,5]

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number,acc)
  }
  return acc
}

console.log(numbersEach(NUMBERS,(number,acc=0) => acc + number))
console.log(numbersEach(NUMBERS,(number,acc=0) => acc - number))
console.log(numbersEach(NUMBERS,(number,acc=1) => acc * number))