// This is your test publishable API key.
const stripe = Stripe("pk_test_51P3k7mSHcSLg6UQOuQNMsGUplZxLFeEhxwnkuZbzH1cUozGRw9H2VH5emUpvT1crVVvLbiW8SaF7dPDFGHRM5ovp00XnJSMcW3");

initialize();

// Create a Checkout Session
async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}