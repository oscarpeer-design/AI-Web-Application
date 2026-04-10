function Header() {
    return (
        <header>
            <h1>Warehouse Valuation Application</h1>
        </header>
    );
}

function LocationLabel() {
    return (
        <label>Choose a location in Sydney</label>
    );
}
function LocationDropDown({ value, onChange }) {
    const suburbMap = {
        "South Sydney": ["Alexandria", "Botany", "Mascot", "Banksmeadow"],
        "Inner West": ["Marrickville", "St Peters", "Tempe"],
        "Central West": ["Eastern Creek", "Erskine Park", "Wetherill Park", "Huntingwood"],
        "South West": ["Moorebank", "Liverpool", "Prestons", "Ingleburn"],
        "Outer West": ["Penrith", "St Marys", "Mount Druitt"]
    };

    return (
        <select value={value} onChange={onChange}>
            {Object.entries(suburbMap).map(([region, suburbs]) => (
                <optgroup key={region} label={region}>
                    {suburbs.map(suburb => (
                        <option key={suburb} value={suburb}>
                            {suburb}
                        </option>
                    ))}
                </optgroup>
            ))}
        </select>
    );
}
function Button({ onClick }) {
    return <button onClick={onClick}>
        Calculate Financials
    </button>;
}

export {Header, Button, LocationLabel, LocationDropDown};