import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import CommentIcon from '@mui/icons-material/Comment';
import { useState } from 'react';
import DeleteIcon from '@mui/icons-material/Delete';
export default function CheckboxList(props) {

    const [checked, setChecked] = useState([]);

    function checking(e) {

        if (e.target.checked) {
            if (!checked.includes(e.target.id)) {
                let newChecked = [...checked, e.target.id];
                setChecked(newChecked);
            }

        } else {
            const newch = checked.filter((id) => id != e.target.id);
            setChecked(newch);
        }
    }
    if (props.array.length == 0) {
        return (
            <p>No Tasks Yet!</p>
        )
    }
    return (
        <List sx={{ width: '100%', maxWidth: 360 }}>
            {props.array.map((value) => {
                const labelId = `checkbox-list-label-${value}`;

                return (
                    <ListItem
                        key={value.id}
                        secondaryAction={
                            <IconButton edge="end" aria-label="comments">
                                <DeleteIcon />
                            </IconButton>
                        }
                        disablePadding
                    >
                        <ListItemButton>
                            <ListItemIcon>
                                <Checkbox
                                    id={value.id} 
                                    checked={checked.indexOf(value) !== -1}
                                    type="checkbox" 
                                    className="t" 
                                    onChange={checking}/>
                            </ListItemIcon>
                            <ListItemText id={labelId} primary={value.name} />
                        </ListItemButton>
                    </ListItem>
                );
            })}
        </List>
    );
}
