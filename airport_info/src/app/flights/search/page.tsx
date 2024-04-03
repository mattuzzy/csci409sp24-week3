export default function FlightSearch({ params }: { params: { origin: string, dest: string } }): JSX.Element {
    return (
        <div>Searching for flights from {params.origin} to {params.dest}</div>
    );
}