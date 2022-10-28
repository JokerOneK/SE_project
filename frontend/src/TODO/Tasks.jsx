import React from "react";
import DeleteIcon from '@mui/icons-material/Delete';
import { useState } from "react";
import { Button, ButtonGroup } from '@mui/material';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';

import Alert from '@mui/material/Alert';

function Tasks(props) {
    const array = props.array;
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

    if (array.length == 0) {
        return (
            <Alert severity="info">There is no tasks!</Alert>
        )
    }
    return <div className="list">
        <List sx={{ width: '100%', maxWidth: 360 }}>
            {array.map(task =>
                <ListItem
                    key={task.id}
                    secondaryAction={
                        <IconButton edge="end" aria-label="comments">
                            <DeleteIcon onClick={() => props.deleteTask(task)} />
                        </IconButton>
                    }
                    disablePadding
                >
                    <ListItemButton>
                        <ListItemIcon>
                            <Checkbox id={task.id} type="checkbox" className="t" onChange={checking} />
                        </ListItemIcon>
                        <ListItemText className="text_item">{task.name}</ListItemText>
                    </ListItemButton>
                </ListItem>
            )}
        </List>


        <ButtonGroup variant="contained" aria-label="outlined primary button group">
            <Button onClick={() => props.deleteSelected(checked)}>Delete Selected</Button>
            <Button onClick={() => props.deleteAll()}>Delete All</Button>
        </ButtonGroup>
    </div>
}
export default Tasks;