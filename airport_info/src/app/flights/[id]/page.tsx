export default function FlightInfo({ params }: { params: { id: string } }): JSX.Element {
    return (
        <div>Hello from Flight # {params.id}</div>
    );
}