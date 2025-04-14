import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

const App = () => (
  <div className="p-4">
    <h1 className="text-2xl mb-4">Guac Dashboard</h1>
    <ul>
      <li><a href="http://localhost:8080/guacamole/#/client/minipc4" className="text-blue-500">minipc4</a></li>
    </ul>
  </div>
)

ReactDOM.createRoot(document.getElementById('root')).render(<App />)