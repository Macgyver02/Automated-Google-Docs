import React, { useState } from 'react';
import axios from 'axios';

function DocumentCreator() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/create-document', { title, content });
      alert(`Document created with ID: ${response.data.documentId}`);
    } catch (error) {
      console.error('Error creating document:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Document Title"
      />
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Document Content"
      />
      <button type="submit">Create Document</button>
    </form>
  );
}

export default DocumentCreator;