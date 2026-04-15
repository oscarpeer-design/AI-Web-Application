import { useEffect, useState } from "react";
import { Header, Button, LocationLabel, LocationDropDown } from "./components.jsx";
import "./App.css";

function App() {
    const [result, setResult] = useState(null);

    const [marketCap, setMarketCap] = useState("");
    const [area, setArea] = useState("");
    const [clearance, setClearance] = useState("");
    const [location, setLocation] = useState("Alexandria");

    useEffect(() => {
        fetch("/api/data")
            .then(res => res.json())
            .then(data => console.log(data)); //debugging output
    }, []);

    const errorMap = {
        a: "Market Cap Rate invalid",
        b: "Lettable Area invalid",
        c: "Clearance invalid",
        d: "Location not recognised",
        e: "Market Cap Rate is outside conventional range (between 2% and 15%)"
    };

    const handleSubmit = () => {
        fetch("/api/valuate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                marketCap,
                area,
                clearance,
                location
            })
        })
            .then(res => res.json())
            .then(data => {
                //setMessage(JSON.stringify(data)); //debugging output
                setResult(data);
            })
            .catch(err => console.error(err));
    };

    return (
        <div className="container">
            <Header />

            <section>
                <input
                    type="text"
                    placeholder="Enter Market Capitalisation Rate"
                    value={marketCap}
                    onChange={e => setMarketCap(e.target.value)}
                />
            </section>

            <section>
                <input
                    type="text"
                    placeholder="Enter Lettable Area"
                    value={area}
                    onChange={e => setArea(e.target.value)}
                />
            </section>

            <section>
                <input
                    type="text"
                    placeholder="Enter Warehouse Clearance"
                    value={clearance}
                    onChange={e => setClearance(e.target.value)}
                />
            </section>

            <section>
                <LocationLabel />
                <LocationDropDown
                    value={location}
                    onChange={e => setLocation(e.target.value)}
                />
            </section>

            <Button onClick={handleSubmit} />

            {/*<p>{message}</p>* debugging output */} 

            {result && (
                <div className="results">
                    <h2>Valuation Results</h2>

                    <p><strong>Annual Rent:</strong> ${ (result["annual_rent"]?? 0).toLocaleString()}</p>

                    <p><strong>NOI:</strong> ${ (result["NOI"]?? 0).toLocaleString()}</p>

                    <p><strong>Property Value:</strong> ${ (result["value"]?? 0).toLocaleString()}</p>

                    <p><strong>Net Yield:</strong> { (result["yield"]?? 0).toFixed(2)}%</p>

                    <p><strong>Confidence Score:</strong> { (result["score"]?? 0)}</p>

                    {result["errors"] && (
                        <p style={{ color: "red" }}>
                            <strong>Errors:</strong> { result["errors"]}
                        </p>
                    )}

                    {result.errors && (
                        <div className="error-box">
                            {result.errors.split("").map(e => (
                                <div key={e}> {errorMap[e]}</div>
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

export default App;

// TO SET CHANGES: go into Powershell and
// type: cd "C:\Users\Oscar\Source\repos\AI-Web-Application\frontend"
// and then: npm.cmd run build

