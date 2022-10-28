import React from 'react';
import { useState } from 'react';
import { TextField, Button } from '@mui/material';
const MyInput = (props) =>{
const [value, setvalue] = useState();
function adding(){
    if(value!=undefined){
        props.addTask(value);
    }
    setvalue('');
}
return(
    

    <div className='input-conteiner'>
        <TextField id="outlined-basic" label="Enter new Task" variant="standard" className='Input-area' value={value} onChange={((e)=>setvalue(e.target.value))}/>
        <Button variant="contained" onClick={adding} size="large" className='buttonAdd'>ADD TASK</Button>
    </div>
    
);
}

export default MyInput;