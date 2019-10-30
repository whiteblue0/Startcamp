/*// primitve(원시) 타입
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8 //10^8
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number
console.log(a,b,c,d,e,f,g)


// string
const sentence1 = 'Ask and go to the blue' // single
const sentence2 = "Ask and go to the blue" // double
const sentence3 = `Ask and go to the blue` // backtick
console.log(sentence1)
console.log(sentence2)
console.log(sentence3)

// double quotation 사용시 줄바꿈 불가 -> 백틱 이용
const word = "안녕
하세요"
const word = "안녕\n하세요"


const word1 = `안녕
하세요`
console.log(word1)

// 백틱 사용 -> 줄바꿈, 문자열 사이에 변수도 넣을 수 있다. 단, 이스케이프 문자열 사용불가

const word2 = `안녕
하세요`
console.log(word2)

const age = 10
const message = `홍길동은 ${age}
세 입니다.`
console.log(message)


const happy = 'Will you join us?'
const hacking = 'Happy' + 'Hacking' + '!'
console.log(happy,hacking)


const truthy = true
const falsy = false
console.log(truthy,falsy)
console.log(typeof truthy)
console.log(typeof falsy)


console.log(typeof null)
console.log(typeof undefined)

console.log(null == undefined)
console.log(null === undefined)


let c = 0
c += 10
console.log(c)
c++
console.log(c)
c--
console.log(c)

// 비교 연산자
console.log(3>2)
console.log(3<2)

console.log('A'<'B')
console.log('Z'<'a')
console.log('가'<'나')


// 동등 비교 연산자 (==)

const a = 1
const b = '1'
console.log(a == b)
console.log(a != b)

// 자동 형변환 예시

console.log(8*null)
console.log("5"-1) // 4(number)
console.log("5"+1) //51(string)
console.log("five"*2) //NaN

const a = 1
const b = "1"

console.log(a === b)
console.log(a === Number(b))


// 논리 연산자
// and
console.log(true && false) // false
console.log(true && true) // true
console.log(1 && 0)
console.log(1 && 1)
console.log(4 && 7)

// or
console.log(false || true)
console.log(false || false)

console.log(1 || 0)
console.log(0 || 1)
console.log(4 || 7)
// not
console.log(!true)
console.log(!false)

*/

// 삼항연산자
// 가장 앞의 boolean 값이 참이면 : 앞의 값이 반환되고 반대일 경우에 : 뒤의 값이 반환

console.log(true ? 1:2)
console.log(false ? 1:2)
console.log('justin' ? 'nice': 'awesome')

// 삼항연산의 결과를 변수에 할당할 수 있다
const result = Math.PI > 4 ? "Yeap":"Nope" 
console.log(result)

