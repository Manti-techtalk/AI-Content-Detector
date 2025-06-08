import React from 'react'

const page = () => {
  return (
    <div className="container">
      <p className='h1 text-center mt-5 border'>
        AI CONTENT DETECTOR TOOL 
      </p>
      <div className="row">
        <div className="col-md-6 offset-md-3">
          <p className='h4 text-center mt-5'>
            Paste your content below to detect if it deflects as AI-generated content.
          </p>
          <textarea className='form-control mt-5' rows="10"></textarea>
          <button className='btn btn-primary mt-3'>Detect AI Content</button>
        </div>
      </div>
    </div>
  )
}

export default page
