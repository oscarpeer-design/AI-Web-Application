import { useEffect, useState } from "react";
import { Header, Button, LocationLabel, LocationDropDown } from "./components.jsx";
import "./App.css";

function App() {
    const [message, setMessage] = useState("");

    const [marketCap, setMarketCap] = useState("");
    const [area, setArea] = useState("");
    const [clearance, setClearance] = useState("");
    const [location, setLocation] = useState("South Sydney");

    useEffect(() => {
        fetch("/api/data")
            .then(res => res.json())
            .then(data => setMessage(data.message));
    }, []);

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
                setMessage(JSON.stringify(data));
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
                    on_change={e => setLocation(e.target.value)}
                />
            </section>

            <Button onClick={handleSubmit} />

            <p>{message}</p>
        </div>
    );
}

export default App;

// TO SET CHANGES: go into Powershell and
// type: cd "C:\Users\Oscar\Source\repos\AI-Web-Application\frontend"
// and then: npm.cmd run build