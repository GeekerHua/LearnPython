
function print(s){
    console.log(s);
}

var sPi = Math.PI;
var iNum = Math.floor(5.65);
var iNum2 = Math.ceil(5.65);

print('sPi = '+ sPi)
print('sNum = '+ iNum)
print('sNum2 = '+ iNum2)


print('------基础的自定义对象--------')
// 自定义对象
var oPerson01 = new Object();

oPerson01.name = 'Tom';
oPerson01.age = 19;

oPerson01.talk = function(s) {
    print('我会说 ' + s);
}

print('我的年龄是' + oPerson01.age);
oPerson01.talk('hello!');

print('------语义化的自定义对象--------')
var oPerson02 = {
    name: 'jack',
    age: '22',
    talk: function(s){
        print(this.name + '也可以说' + s);
    }
}

print(oPerson02.name + '今年' + oPerson02.age + '岁了');
oPerson02.talk('hello world!');
