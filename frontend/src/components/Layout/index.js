import React from 'react'
import Header from '@/components/Header'
import Main from '@/components/Main'
import './Layout.css'

class Layout extends React.Component {
    render() {
        return (
            <div className="Layout">
                <Header />
                <Main />
            </div>
        );
    }
}

export default Layout;