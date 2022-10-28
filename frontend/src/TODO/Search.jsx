import React from "react";
import { useMemo, useState } from "react";    
import { TextField } from "@mui/material";

function Search({searchQuery,setSearchQuery}){

    return(<>
        <TextField placeholder='Search...'
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        />
        
        </>
        
    )

}


export default Search;