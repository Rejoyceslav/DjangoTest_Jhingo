import React from "react";
import AppBar from '@material-ui/core/AppBar'
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";
import brandLogo from '.././images/brandLogo.png';
import LogoSVG from "./LogoSVG";
import ".././style.css";

const useStyles = makeStyles((theme) => ({
    appBar: {
        borderBottom: '1px solid ${theme.palette.divider}',
    },
}));

function Header() {
    const classes = useStyles();
    return (
        <React.Fragment>
            <CssBaseline />
            <AppBar position = 'static' color = 'white' style={{backgroundColor: '#000a3f'}} elevation = {0} className = {classes.appBar}>
                <Toolbar>  
                    {/* <LogoSVG /> */}
                    <div>
                        <img src={brandLogo} alt="EMART" className="brand"/>
                    </div>
                </Toolbar>
            </AppBar>
        </React.Fragment>
    );
}

export default Header;