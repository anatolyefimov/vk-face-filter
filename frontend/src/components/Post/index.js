import React from 'react';
import './Post.css';

class Post extends React.Component {
    render() {
        return ( 
            <div className="Post">
                {this.props.text}
                {this.props.photos.map((photo, index) => <a href={photo}  key={index}> Фото {index + 1} </a>)}
            </div> 
        );
    };
}

export default Post;