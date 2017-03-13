var count = 1;
function printLine() {
    console.log('-----' + count + '----');
    count++;
}
var sTr = '12';
var sTr2 = '36.2';
var iNum = 24;

console.log(sTr+sTr2 + iNum);
printLine();
console.log(Number(sTr2) + iNum);
console.log(parseInt(sTr) + parseInt(sTr2));
console.log(parseInt('124abc3'));
printLine();
if (!isNaN(parseInt('99'))) {
    console.log('isNaN');
}
printLine();
sTr3 = "1234567".split('').reverse().join('');
console.log(sTr3);
console.log(0.1+0.2);       // 0.3000000000000004
console.log((0.1*100 + 0.2*100)/100);

