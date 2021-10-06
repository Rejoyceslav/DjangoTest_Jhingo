import React from "react";
import Typography from "@material-ui/core/Typography";

function LogoSVG() {
    return (
        <React.Fragment>
            <div style={{paddingTop: 0 + 'px'}}>
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="38.000000pt" height="38.000000pt" viewBox="0 0 138.000000 138.000000"
                preserveAspectRatio="xMidYMid meet">
                    <rect x="1" y="1" width="135.000000pt" height="135.000000pt" fill="#fbe901"/>
                    <g transform="translate(0.000000,138.000000) scale(0.100000,-0.100000)"
                    fill="#000a3f" stroke="none">
                        <path d="M0 690 l0 -690 690 0 690 0 0 690 0 690 -690 0 -690 0 0 -690z m1340
                        0 l0 -650 -650 0 -650 0 0 650 0 650 650 0 650 0 0 -650z"/>
                        <path d="M605 1195 c-55 -30 -95 -77 -111 -133 -18 -59 -13 -94 21 -163 32
                        -63 40 -112 25 -163 -24 -87 -108 -155 -191 -156 -121 -1 -212 -91 -212 -210
                        0 -63 17 -101 65 -147 42 -40 76 -53 140 -53 72 0 132 31 174 91 39 54 117 99
                        172 99 60 0 127 -37 183 -102 60 -69 97 -88 169 -88 67 0 107 18 152 68 74 82
                        74 195 -1 275 -37 41 -74 58 -149 68 -124 18 -192 82 -200 189 -4 48 1 69 23
                        117 41 89 43 141 10 208 -37 77 -86 108 -174 113 -47 2 -75 -2 -96 -13z"/>
                    </g>
                </svg>
            </div>
            <div>
                <Typography variant='h4' style={{color: 'white', lineHeight: 30 + 'px', marginTop: 0 + 'px'}} noWrap>
                    EMART
                </Typography>
                <Typography style={{color: '#fbe901', lineHeight: 11 + 'px', marginBottom: 6 + 'px'}} noWrap>
                    serwis dmuchaw
                </Typography>
            </div>
        </React.Fragment>
    );
}

export default LogoSVG; 