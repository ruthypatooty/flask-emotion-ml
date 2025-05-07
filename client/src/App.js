import React, {useState, useEffect} from 'react'

function App() {
  const [inputText, setInputText] = useState('');
  const [emotion, setEmotion] = useState('');
  const [isSubmit, setIsSubmit] = useState(false);
  const [responseMessage, setResponseMessage] = useState('');


  useEffect(() => {
    fetch("/upload").then(
      res =>res.text())
      .then(data => {
        // setInputText(data);
        console.log(data);

      })
  });

  const handleSubmit= async()=>{
    setIsSubmit(true);
    try{
      const resp = await fetch("/getText",{
          method: 'POST',
          headers: {
            'Content-type':'application/json'
          },
          body: JSON.stringify({text:inputText})
      })

      const data = await resp.json();
  
      if(data.success){
        setEmotion(data.emotion)
        setResponseMessage('')
      }
      else
        setResponseMessage('Error')
    }
    catch{

      setResponseMessage("error with server");
      setIsSubmit(false);
    }finally{
      setIsSubmit(false);
    }
  }

  const handleInputChange =(e) =>{
    setInputText(e.target.value);
  }

  return (
    <div className="container">
      <input
        type="text"
        value={inputText}
        onChange={handleInputChange}
        placeholder="How are you feeling?..."
        disabled={isSubmit}
      />
      <button
        onClick={handleSubmit}
        disabled={isSubmit}
      >
        {isSubmit ? 'Analyzing...' : 'Analyze Emotion'}
      </button>

      {emotion && (
        <div className="result">
          <h3>Detected Emotion:</h3>
          <p>{emotion}</p>
        </div>
      )}

      {responseMessage && (
        <div className="error-message">
          {responseMessage}
        </div>
      )}
    </div>
  );
}

export default App;
