import { useEffect, useState } from "react";
import { Header, Button, MCapField, AreaField, ClearanceField, LocationLabel, LocationDropDown} from "./components.jsx";
import "./App.css";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch("/api/data")
            .then(res => res.json())
            .then(data => setMessage(data.message));
    }, []);

    return (
        <div className="container">
            <Header></Header>

            <section>
                <MCapField></MCapField>
            </section>
            <section>
                <AreaField></AreaField>
            </section>
            <section>
                <ClearanceField></ClearanceField>
            </section>
            <section>
                <LocationLabel></LocationLabel>
                <LocationDropDown></LocationDropDown>
            </section>
                <Button></Button>
            <p>{message}</p>
        </div>
    );
}
// TO SET CHANGES: go into Powershell and
// type: cd "C:\Users\Oscar\Source\repos\AI-Web-Application\frontend"
// and then: npm.cmd run build
export default App;