// join方法，将数组拼成字符串
var aR1 = [1,5,2,7];
console.log(aR1.join('-'));

// push
console.log(aR1.push('haha'));
console.log(aR1);
// pop
console.log('------');
console.log(aR1.pop());
console.log(aR1);

console.log('------');
console.log(aR1.unshift(333));
console.log(aR1.reverse());
console.log(aR1);

console.log('------');
console.log(aR1.indexOf(1));
console.log(aR1.lastIndexOf(333));

console.log('------');
// 在数组中增加或者删除成员
console.log(aR1.splice(2,2,444,6666));
console.log(aR1);

// 数组去重
var aLi = [1,2,4,5,1,4,7,2,4];
var aLi2 = [];
for (var i = 0; i < aLi.length; i++) {
    if (aLi.indexOf(aLi[i]) == i) {
        aLi2.push(aLi[i])
    }
}
console.log(aLi2);