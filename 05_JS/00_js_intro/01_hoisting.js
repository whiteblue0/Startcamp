// Hoisting!
// 나중에 선언된 변수를 참조 할 수 있음
// 함수 or statement 최상단으로 올려지는 것(hosting)
// 변수와 함수를 위한 메모리를 확보하는 과정


// var
// console.log(a)
// var a = 10
// console.log(a)
/* var hoisting
1. 선언이 최상단으로 올라감
2. 선언이 최상단으로 올라갔기 때문에 에러가 나지 않고 undefined가 출력      *JS에서는 var 변수를 선언할 때 값을 넣어주지 않으면 undefined를 자동으로 넣음
3. 할당은 그 뒤에 이루어짐
4. 최종 출력
*/
// let
console.log(b)
let b = 10
console.log(b)
/* let 이 hoisting 되는 과정
2. 에러
3. 할당
4. 출력
*/