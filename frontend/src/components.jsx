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

export {Header, Button, MCapField, AreaField, ClearanceField};