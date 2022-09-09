//creamos array
const arrayNumbers = [4, 30, 7, 5, 9, 7, 2, 4, 1, 3, 2];

//creamos funcion
function Sort (arrayNumbers){
    //clonamos el array
    let newArray = [...arrayNumbers];

    //sacamos la longitud del array
    let dataLen = newArray.length;
    
    //Creamos un ciclo for para recorrer el array
    for(let index = 0; index < dataLen; index++){
        //Creamos un ciclo for para organizar los numeros dentro del array
        for(let subIndex = 0; subIndex < dataLen; subIndex++){
            //Validamos si el numero iterado es mayor al siguiente numero a iterar
                if(newArray[subIndex] > newArray[subIndex+1]){
                    //Guardamos el siguiente numero
                    let swapElement = newArray[subIndex+1];
                    //cambiamos de posicion los numeros
                    newArray[subIndex+1] = newArray[subIndex];
                    newArray[subIndex] = swapElement;
                }
        }
    }
    return newArray;
}

arrayNumbers.sort()

console.log("Sort menor a mayor:", Sort(arrayNumbers));