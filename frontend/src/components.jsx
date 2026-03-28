function Header() {
    return (
        <header>
            <h1>AI Web Application</h1>
        </header>
    );
}

function LocationLabel() {
    return (
        <label>Choose a location in Sydney</label>
    );
}
function LocationDropDown({value, on_change}) { 
    return (
        <select value={value} onChange={on_change}>
            <option value="South Sydney">South Sydney</option>
            <option value="Inner West">Inner West</option>
            <option value="Eastern Creek">Eastern Creek</option>
            <option value="Moorebank">Moorebank</option>
            <option value="Outer West">Outer West</option>
            <option value="South West">South West</option>
        </select>
    );
}
function Button({ onClick }) {
    return <button onClick={onClick}>
        Calculate Financials
    </button>;
}

export {Header, Button, LocationLabel, LocationDropDown};