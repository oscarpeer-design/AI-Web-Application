function Header() {
    return (
        <header>
            <h1>AI Web Application</h1>
        </header>
    );
}
function MCapField() {
    return (
        <input type="text" placeholder = "Enter Market Capitalisation Rate"/>
    );
}
function AreaField() {
    return (
        <input type="text" placeholder= "Enter Lettable Area"/>
    );
}
function ClearanceField() {
    return (
        <input type="text" placeholder= "Enter Warehouse Clearance"/>
    );
}
function Button() {
    return (
        <button>
            Calculate Finacials
        </button>
    );
}

function LocationLabel() {
    return (
        <label>Choose a location in Sydney</label>
    );
}
function LocationDropDown() { 
    return (
        <select>
            <option value="South Sydney">South Sydney</option>
            <option value="Inner West">Inner West</option>
            <option value="Eastern Creek">Eastern Creek</option>
            <option value="Moorebank">Moorebank</option>
            <option value="Outer West">Outer West</option>
            <option value="South West">South West</option>
        </select>
    );
}

export {Header, Button, MCapField, AreaField, ClearanceField, LocationLabel, LocationDropDown};