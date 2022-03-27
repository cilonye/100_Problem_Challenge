
function index(){
    const length = document.querySelector('#length').value;
    const d1 = document.querySelector("#d1").value;
    const d2 = document.querySelector("#d2").value;
    const h = document.querySelector("#height").value;
    
    time_1 = emptying_time([length, d1, d2, h])
    
    document.querySelector("#result").value = time_1;
}

function emptying_time([length, d1, d2, h]){
    try{
        time_1 = (0.6*(2/9.81)**0.5*(parseFloat(length)/(parseFloat(h)**0.5))*(parseFloat(d2)**2/(parseFloat(d1)**2)))/60
        time_1 = time_1.toFixed(4);
        return time_1
    } 
    catch(err){
        return "invalid input"
    }   
}

function clearResult(){
    document.querySelector("#result").value = '';    
}

    
    