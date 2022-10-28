import React from "react";
import { FormControl, InputLabel, Select, MenuItem } from "@mui/material";
function Sort({ options, defaultValue, value, onChangingFunc }) {
    return (


        <>
            <FormControl sx={{ m: 1, minWidth: 120 }}>
                <InputLabel id="demo-simple-select-label">Sort</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={value} 
                    label="SORT"
                    onChange={(event) => onChangingFunc(event.target.value)}
                >
                    {options.map(option =>
                    <MenuItem key={option.value} value={option.value}>
                        {option.name}
                    </MenuItem>
                )}
                </Select>
            </FormControl>
        </>

    );
}


export default Sort;