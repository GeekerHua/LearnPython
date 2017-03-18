var date1 = new Date(); //开始时间
for (var a = 0; a < 1000; a++) {
    for (var b = 0; b < 1000; b++) {
        for (var c = 0; c < 1000; c++) {
            if (a ** 2 + b ** 2 == c ** 2 && a + b + c == 1000) {
                console.log(a, b, c);
            }
        }
    }
}
var date2 = new Date(); //结束时间
console.log(date2.getTime() - date1.getTime());