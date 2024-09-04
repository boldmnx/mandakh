export default function ProductReviewDetail({
  params,
}: {
  params: { product_id: string; review_id: string };
}) {
  return (
    <>
      {params.product_id}-тай бүтээгдэхүүний сэтгэгдэл: {params.review_id}
    </>
  );
}
