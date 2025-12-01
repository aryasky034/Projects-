
    console.log("hellow world");
    //alert("hello world");
    // call stack gets created and all the events needed to be executed are pushed into THIS CALL STACK
    // event loop keeps a check on items that needds to be executed
    //global exceution context is where the events runs

    //let
    //var
    //const
    var a = 5;// traditional and avoid in mordern web
    // can be reintialised
    let b = 10;// not used as commanly as const
    //cannot be reintialised
    const c =15;// commonly used for variable declartion 
    b = 12;
    console.log(b);
    let name = "letsupgrade";//string
    let age =20;//numeric
    let scores = [20,12,24];//array
    let isvalid= true;//boolean
    let student={
        name:"rahul",
        age:24,
        scores:[23,232,345],
        pass:true,
    };//object

    const {name1,age1,paas1}=student;
    console.log(name1,age1,paas1);

    console.log(student.name);
    console.log(student.age);
    console.log(student.scores[4]);
    if(student.scores[0] || student.scores[4]<12){
        student.paas=false;
        alert("failed");
    }
    else{
        alert("paas");
    }



    if(age>=18 && age<=24){
        alert("allowed to vote but not marry ");
    }
    else{
        alert("allowed to marry and vote");
    }


    const runs=[12,34,34,45,56,100,56,23,45,56,78];
    for(let i=0; i<=runs.length; i++){
        console.log(runs[i]);

    if(runs[i]>=100){
        console.log("player at "+ i+ "position made a century");
    }
    else if(runs[i]==0){
        console.log("playerat " + i+"got out at tuck");
    }
    else{
        console.log("played well");
    }
    }

// task: grossary discount calculator
// sumtotal all the items spices veggies pepper then apply a discount on total consloe.log the final bill after discount.

//document object model
document.addEventListener("dom content loaded",function(){
    document.getElementById("my name").style.color="green";
    let cards=document.getElementsByClassName("card");
    for(let i=0;i<cards.length;i++){
        cards[i].style.backgroundcolor="dodgerblue";
    }
    let card1=cards[0];
    console.log(cards);
    //card1style.backgroundcolor="yellow";
    document.queryselecter(".card");
    document.queryselecter("#card").style.color="red";
    document.queryselecterall(".card").style.backgroundcolor="grey";
    let cardsquery=(document.queryselector(".card"));
    for(let i=0;i<cards.length;i++){
        cards[i].style.backgroundcolor="grey"
    }
});
function hireme(){
    alert("hey i am available to work");
}
//onclick="hireme()"
//document.addEventListener('click',hireme());
//btn.addEventListener("mouseover",hireme());
//localstorage
// using local storgae create a to do list
//add items 
//remove items
let dosomething1 = ()=>{
    console.log("hello world");
};
let numbe=12;
console.log(`hi thi is back tick${numbe}`);
const obj={...student };
console.log(obj);
const arr1=[1,2,3,0];
const arr2=[...arr1,4,5,6,7];
console.log(arr2);
// map filter and reduce foreach
for(let i =0;i<arr1.length;i++){
    console.log(arr1[i]);
}
arr1.foreach((elen)=>{
    console.log(elen);
});

let newaar1 = arr1.map((elem)=>{
    return elem*2;
});

console.log(newarr);
let filter=arr1.filter((elem)=>{
    return elem % 2==0;
});
let max=arr1.reduce((acc,curr)=>{
    if(acc>curr){
        acc=curr;
    }
    return acc;
},0);
console.log(max);
function getcity(event){
    let city=event.target.value;
    let url="";
    let apikey=`=${city}%appid=${apikey}$units=${metric}}`;
}



async function getwhether(){
    let resp=await fetch(url)
    let data=await resp.json();
    document.getElementById("dynamic").innertext=data.main.temp;
}
getwhether();
//