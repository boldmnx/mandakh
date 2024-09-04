export default function ProductDetail({
  params,
}: {
  params: { product_id: string };
}) {
  return <h1>{params.product_id}</h1>;
}
