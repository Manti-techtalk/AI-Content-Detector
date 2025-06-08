'use client'
import React, { useState, useEffect } from 'react'
import axios from 'axios'

const HISTORY_KEY = 'aiDetectorHistory'

const Page = () => {
  const [inputText, setInputText] = useState("")
  const [result, setResult] = useState("")
  const [confidence, setConfidence] = useState(null)
  const [error, setError] = useState("")
  const [history, setHistory] = useState([])

  useEffect(() => {
    const saved = localStorage.getItem(HISTORY_KEY)
    if (saved) setHistory(JSON.parse(saved))
  }, [])

  useEffect(() => {
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history))
  }, [history])

  const handleClick = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/predict/",
        { input_text: inputText },
        { headers: { 'Content-Type': 'application/json' } }
      )

      const { result, confidence } = response.data
      setResult(result)
      setConfidence(confidence)
      setError("")

      const newEntry = {
        result,
        confidence,
        timestamp: new Date().toLocaleString()
      }
      setHistory(prev => [newEntry, ...prev].slice(0, 10))
    } catch (err) {
      console.error("Error:", err.response?.data || err.message)
      setResult("")
      setConfidence(null)
      setError("Error processing your request.")
    }
  }

  return (
    <div className="container">
      <p className="h1 text-center mt-5 border">
        AI CONTENT DETECTOR TOOL 
      </p>
      <div className="row mt-4">
        {/* Left side: input, button, results */}
        <div className="col-md-7">
          <p className="h4 text-center">
            Paste your content below to detect if it was AI-generated.
          </p>
          <textarea 
            className="form-control mt-3"
            rows="10"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          ></textarea>
          <button onClick={handleClick} className="btn btn-primary mt-3">
            Detect AI Content
          </button>

          {result && confidence !== null && (
            <div className="alert alert-info mt-4 text-center">
              Prediction: <strong>{result}</strong><br />
              Confidence: <strong>{confidence.toFixed(2)}%</strong>
            </div>
          )}

          {error && (
            <div className="alert alert-danger mt-4 text-center">
              {error}
            </div>
          )}
        </div>

        {/* Right side: history */}
        <div className="col-md-5">
          {history.length > 0 && (
            <div className="mt-3">
              <h5 className='h3'>History</h5>
              <ul className="list-group">
                {history.map((entry, idx) => (
                  <li key={idx} className="list-group-item">
                    <strong>{entry.timestamp}:</strong> {entry.result} at {entry.confidence.toFixed(2)}%
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default Page


