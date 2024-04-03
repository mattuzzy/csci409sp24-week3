export default function Airportinfo({ params }: { params: { id: string } }) {
    return (
        <div>Hello From Airport # {params.id}</div>
    );
}